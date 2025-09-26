import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';

import Login from "./Login"
import SignUp from "./SignUp"

function App() {
  

  return (
    <BrowserRouter>
    <Routes>
      <Route path="/login" element={<Login/>} />
      <Route path="/signup" element={<SignUp/>} />
      <Route path="*" element={<Navigate to="/login" replace/>} />
    </Routes>
    </BrowserRouter>
  )
}

export default App;
