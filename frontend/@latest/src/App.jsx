import React from 'react'
import ChatBot from './ChatBot'
import Header from './Header'
import "./App.css"
const App = () => {
  return (
    <div className=''>
      {/* Chat bot */}
      <Header />
      <ChatBot />
    </div>
  )
}
export default App