import './assets/css/App.css'
import Login from './pages/Login'
import { Routes, Route} from 'react-router-dom' 
import Register from './pages/Register'

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register/>} />
      </Routes>
    </>
  )
}

export default App
