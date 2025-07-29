import React ,{ useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Landingpage from './pages/Landingpage'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
       <Landingpage/>        
    </>
  )
}

export default App
