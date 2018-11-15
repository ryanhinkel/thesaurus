import React, { PureComponent } from 'react'

class Clue extends PureComponent {
  render() {
    const { clue, closeTo } = this.props
    return (
      <div className="ma4 tc f2 green">
        {clue ? (
          <span>
            Clue: {clue} for {closeTo}
          </span>
        ) : null}
      </div>
    )
  }
}

export default Clue
