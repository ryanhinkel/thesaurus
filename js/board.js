import React, { PureComponent } from 'react'
import { splitEvery } from 'ramda'

export default class Board extends PureComponent {
  getCardStyles = (word) => {
    const { picked, my_spies, their_spies, assassin, words } = this.props

    if (!picked.includes(word)) {
      return 'bg-light-gray'
    }

    const index = words.indexOf(word)
    if (my_spies.includes(index)) {
      return 'bg-red white'
    } else if (their_spies.includes(index)) {
      return 'bg-blue white'
    } else if (assassin === index) {
      return 'bg-black white'
    } else {
      return 'bg-yellow black'
    }
  }

  render () {
    const { pickWord, words } = this.props

    const rows = splitEvery(5, words)
    return (
      <div className='ma2 ba--white-20 f2'>
        { rows.map((row) => {
          return (
            <div key={row.toString()}>
              { row.map((word) => {
                const cardStyles = this.getCardStyles(word)
                return (
                  <div
                    onClick={() => pickWord(word)}
                    key={word}
                    className={`dib pa2 w5 h3 ${ cardStyles } ma1`}
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
