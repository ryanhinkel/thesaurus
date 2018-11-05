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
  ally: word => "Communication Secured",
  ally: word => <span className='f4'>Communication Secured</span>,
  enemy: word => <span><span>⚠</span><br /><span className='f4'>SECURITY BREACH</span></span>,
  assassin: word => <span><span>⚠</span><br /><span className='f4'>CONNECTION LOST</span></span>,
  civilian: word =>  `${word}?`,
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

  getCardStyles = (team) => {
      return styles[team]
  }

  getCardContent = (word, team) => {
    return content[team](word)
  }

  render () {
    const { pickWord, words } = this.props

    const rows = splitEvery(5, words)
    return (
      <div className='map-background courier pa1 ba--white-20 f3 pa2 ma1 ba bw2 b--green'>
        { rows.map((row) => {
          return (
            <div key={row.toString()}>
              { row.map((word) => {
                const team = this.getCardTeam(word)
                const styles = this.getCardStyles(team)
                const content = this.getCardContent(word, team)
                return (
                  <div
                    onClick={() => pickWord(word)}
                    key={word}
                    className={`dib w-20 v-top`}
                  >
                    <div className={`card ba bw2 ph2 pt4 h4 tc ${ styles } ma1`}>
                      { content }
                    </div>
                  </div>
                )
              }) }
            </div>
          )
        }) }
      </div>
    )
  }
}
