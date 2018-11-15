import React, { PureComponent } from 'react'

class GameMessage extends PureComponent {
  render() {
    const { message, className } = this.props

    const layoutStyles = 'absolute top-2 left-2 right-2 bottom-2'
    const fontStyles = 'courier f1 tc '
    const outerMessageStyles = `game-message pa2 ${layoutStyles} ${fontStyles} ${className}`
    const innerMessageStyles = `ba bw2 h-100 w-100 pa6 ${className}`

    return (
      <div className={outerMessageStyles}>
        <div className={innerMessageStyles}>{message}</div>
      </div>
    )
  }
}

export default GameMessage
