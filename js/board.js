import React, { PureComponent } from 'react'
import { splitEvery } from 'ramda'

export default class Board extends PureComponent {
  getCardStyles = (word) => {
    const { picked, my_spies, their_spies, assassin, words } = this.props

    if (!picked.includes(word)) {
      return 'bg-light-gray black'
    }

    const index = words.indexOf(word)
    if (my_spies.includes(index)) {
      return 'bg-mid-gray dark-red'
    } else if (their_spies.includes(index)) {
      return 'bg-mid-gray light-blue'
    } else if (assassin === index) {
      return 'bg-white white'
    } else {
      return 'bg-near-white green'
    }
  }

  render () {
    const { pickWord, words } = this.props

    const rows = splitEvery(5, words)
    return (
      <div className='avenir ma2 ba--white-20 f2'>
        { rows.map((row) => {
          return (
            <div key={row.toString()}>
              { row.map((word) => {
                const cardStyles = this.getCardStyles(word)
                return (
                  <div
                    onClick={() => pickWord(word)}
                    key={word}
                    className={`dib pa2 pv4 w5 h4 tc ${ cardStyles } ma1`}
                  >{ word }</div>
                )
              }) }
            </div>
          )
        }) }
      </div>
    )
  }
}
