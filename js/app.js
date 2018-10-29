import React, { PureComponent } from 'react'
import { map } from 'ramda'
import { post } from 'axios'

import Board from './board'

const getWords = (words, indices, excludeWords) => {
  const excludeFilter = n => !excludeWords.includes(words[n])
  return map(
    index => words[index],
    indices.filter(excludeFilter),
  )
}

export default class App extends PureComponent {
  constructor () {
    super()
    this.state = {
      picked: [],
      clue: '',
      closeTo: 0,
    }
  }

  componentDidMount () {
    this.getClue()
  }

  getClue = () => {
    const { data: { my_spies, their_spies, assassin, words } } = this.props
    const { picked, closeTo } = this.state

    if (closeTo > 0) {
      return null
    }

    const bad_words = getWords(words, their_spies, picked)
    const good_words = getWords(words, my_spies, picked)
    const really_bad_words = [words[assassin]]

    post('./clue', { bad_words, good_words, really_bad_words })
      .then((response) => {
        const { word: clue, close_to: closeTo, allies } = response.data
        console.log(clue, closeTo, allies.toString())
        this.setState({ clue, closeTo, allies })
      })
  }

  pickWord = (word) => {
    this.setState(
      state => {
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
      },
      this.getClue
    )
  }

  render () {
    const { data } = this.props
    const { picked, clue, closeTo } = this.state
    return (
      <div className='bg-near-black h-100 w-100'>
        <Board picked={picked} pickWord={this.pickWord} {...data} />
        <div className='ma4 tc f2 courier green'>
          { clue
            ? <span>Clue: { clue } for { closeTo }</span>
            : null }
        </div>
      </div>
    )
  }
}
