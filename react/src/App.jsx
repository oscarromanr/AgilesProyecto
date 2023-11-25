import './assets/css/App.css'
import Login from './pages/Login'
import { Routes, Route} from 'react-router-dom' 
import RegisterCourse from './pages/RegisterCourse'

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/registerCourse" element={<RegisterCourse/>} />
      </Routes>
    </>
  )
}

export default App
