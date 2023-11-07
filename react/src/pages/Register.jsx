import '../assets/css/pages/register.css'
import RegisterForm from "../components/register/RegisterForm/RegisterForm";

const Register = () => {
    return (
        <div className="page-container">
            <div className="aside img-container">
                <div className="logo">
                </div>
            </div>
            <div className="main">
                <RegisterForm />
            </div>
        </div>
    );
};

export default Register;