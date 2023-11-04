import '../assets/css/pages/login.css'
import LoginForm from "../components/login/LoginForm/LoginForm";

const Login = () => {
    return (
        <div className="page-container">
            <div className="aside img-container">
                <div className="logo">
                </div>
            </div>
            <div className="main">
                <LoginForm />
            </div>
        </div>
    );
};

export default Login;