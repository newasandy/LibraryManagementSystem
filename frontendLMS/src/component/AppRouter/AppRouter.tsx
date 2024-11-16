
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import LoginPage from '../login/LoginPage'
import SignUpPage from '../signup/SignUpPage'

const AppRouter = () => {
    return (
        <BrowserRouter>
            <Routes>

                <Route path='/login' element={<LoginPage />} />
                <Route path='' element={<SignUpPage />} />
            </Routes>
        </BrowserRouter>


    )
}

export default AppRouter
