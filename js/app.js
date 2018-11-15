import React, { PureComponent } from 'react'
import { map } from 'ramda'
import { post } from 'axios'

import Board from './board'

const getWords = (words, indices, excludeWords) => {
  const excludeFilter = n => !excludeWords.includes(words[n])
  return map(index => words[index], indices.filter(excludeFilter))
}

class GameMessage extends PureComponent {
  render() {
    const { message, className } = this.props
    const layoutStyles = 'absolute top-2 left-2 right-2 bottom-2'
    const fontStyles = 'courier f1 tc '

    return (
      <div
        className={`game-message pa2 ${layoutStyles} ${fontStyles} ${className}`}
      >
        <div className={`ba bw2 h-100 w-100 pa6 ${className}`}>{message}</div>
      </div>
    )
  }
}

export default class App extends PureComponent {
  constructor() {
    super()
    this.state = {
      picked: [],
      allies: [],
      clue: '',
      closeTo: 0,
    }
  }

  componentDidMount() {
    this.getClue()
  }

  getClue = () => {
    const {
      data: { my_spies, assassin, words },
    } = this.props
    const { picked, closeTo } = this.state

    if (closeTo > 0) {
      // Do nothing if we stil have a clue in state
      return null
    }

    const not_my_spies = words
      .map((_, i) => i)
      .filter(i => !my_spies.includes(i))
    const bad_words = getWords(words, not_my_spies, picked)
    const good_words = getWords(words, my_spies, picked)
    const really_bad_words = [words[assassin]]

    post('./clue', { bad_words, good_words, really_bad_words }).then(
      response => {
        const { word: clue, close_to: closeTo, allies } = response.data
        console.log(clue, closeTo, allies.toString()) // eslint-disable-line
        this.setState({ clue, closeTo, allies })
      },
    )
  }

  pickWord = word => {
    this.setState(state => {
      const picked = state.picked.concat(word)
      const wordLower = word.toLowerCase()
      if (state.allies.includes(wordLower)) {
        return {
          closeTo: state.closeTo - 1,
          allies: state.allies.filter(w => w !== word),
          picked,
        }
      } else {
        return { picked }
      }
    }, this.getClue)
  }

  getGameProgress = () => {
    const {
      data: { my_spies, their_spies, assassin, words },
    } = this.props
    const { picked } = this.state

    const pickedIndexes = picked.map(word => words.indexOf(word))

    const securityBreaches = their_spies.filter(spy =>
      pickedIndexes.includes(spy),
    ).length
    const gameLost = pickedIndexes.includes(assassin)
    const gameWon =
      my_spies.filter(spy => pickedIndexes.includes(spy)).length ===
      my_spies.length

    return { securityBreaches, gameLost, gameWon }
  }

  render() {
    const { data } = this.props
    const { picked, clue, closeTo } = this.state
    const { gameLost, gameWon } = this.getGameProgress()

    return (
      <div className="bg-near-black h-100 w-100 pa1">
        <Board picked={picked} pickWord={this.pickWord} {...data} />
        <div className="ma4 tc f2 courier green">
          {clue ? (
            <span>
              Clue: {clue} for {closeTo}
            </span>
          ) : null}
        </div>
        {gameWon ? (
          <GameMessage
            message="Well done, Jim"
            className="bg-black green win"
          />
        ) : null}

        {gameLost ? (
          <GameMessage
            message="You have failed Jim"
            className="yellow bg-black loss"
          />
        ) : null}
      </div>
    )
  }
}
