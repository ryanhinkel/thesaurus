import React from 'react'
import { render } from 'react-dom'

import App from './app.js'

import '../sass/index.scss'

render(<App data={data} />, document.getElementById('app'))
