import React, { PureComponent } from 'react'
import { splitEvery } from 'ramda'

const styles = {
  unknown: 'unknown b--green green',
  ally: 'ally bg-dark-green green',
  enemy: 'enemy bg-dark-gray yellow',
  assassin: 'assassin bg-yellow',
  civilian: 'civilian b--black',
}

const content = {
  unknown: word => word,
  ally: word => (
    <span>
      <span>{word}</span>
      <br />
      <span>Communication Secured</span>
    </span>
  ),
  enemy: () => (
    <span>
      <span>⚠</span>
      <br />
      <span>SECURITY BREACH</span>
    </span>
  ),
  assassin: word => (
    <span>
      <span>⚠ {word}</span>
      <br />
      <span>CONNECTION LOST</span>
    </span>
  ),
  civilian: word => `${word}?`,
}

export class BoardWord extends PureComponent {
  onClick = () => {
    const { onClick, word } = this.props
    onClick(word)
  }

  render() {
    const { styles, children } = this.props

    return (
      <div onClick={this.onClick} className={`dib w-20 v-top`}>
        <div className={`card ba bw2 ph2 pt3 h3 tc ${styles} ma1`}>
          {children}
        </div>
      </div>
    )
  }
}

export default class Board extends PureComponent {
  getCardTeam = word => {
    const { picked, my_spies, their_spies, assassin, words } = this.props
    const index = words.indexOf(word)

    if (!picked.includes(word)) {
      return 'unknown'
    } else if (my_spies.includes(index)) {
      return 'ally'
    } else if (their_spies.includes(index)) {
      return 'enemy'
    } else if (assassin === index) {
      return 'assassin'
    } else {
      return 'civilian'
    }
  }

  getCardStyles = team => {
    return styles[team]
  }

  getCardContent = (word, team) => {
    return content[team](word)
  }

  render() {
    const { pickWord, words } = this.props
    const rows = splitEvery(5, words)

    return (
      <div className="map-background courier ba--white-20 f5 pa2 ma1 ba bw2 b--green">
        {rows.map(row => {
          return (
            <div key={row.toString()}>
              {row.map(word => {
                const team = this.getCardTeam(word)
                const props = {
                  word,
                  styles: this.getCardStyles(team),
                  children: this.getCardContent(word, team),
                  onClick: pickWord,
                }
                return <BoardWord key={word} {...props} />
              })}
            </div>
          )
        })}
      </div>
    )
  }
}
