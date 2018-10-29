import React, { PureComponent } from 'react'
import { splitEvery } from 'ramda'

const styles = {
  unknown: 'gray',
  ally: 'bg-dark-gray dark-red',
  enemy: 'bg-light-blue light-blue b--light-blue',
  assassin: 'white',
  civilian: 'b--green green',
}

export default class Board extends PureComponent {
  getCardStyles = (word) => {
    const { picked, my_spies, their_spies, assassin, words } = this.props
    const index = words.indexOf(word)

    if (!picked.includes(word)) {
      return styles['unknown']
    } else if (my_spies.includes(index)) {
      return styles['ally']
    } else if (their_spies.includes(index)) {
      return styles['enemy']
    } else if (assassin === index) {
      return styles['assassin']
    } else {
      return styles['civilian']
    }
  }

  render () {
    const { pickWord, words } = this.props

    const rows = splitEvery(5, words)
    return (
      <div className='avenir pa1 ba--white-20 f2'>
        { rows.map((row) => {
          return (
            <div key={row.toString()}>
              { row.map((word) => {
                const cardStyles = this.getCardStyles(word)
                return (
                  <div
                    onClick={() => pickWord(word)}
                    key={word}
                    className={`dib pa2 pv4 w5 h4 tc ba ${ cardStyles } ma1`}
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
