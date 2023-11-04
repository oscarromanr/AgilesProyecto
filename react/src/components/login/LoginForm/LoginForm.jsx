import './LoginForm.css';
import { useForm } from "../../../hooks/useForm";
import LoginService from '../../../services/loginService';
import { useNavigate } from 'react-router-dom';

const LoginForm = () => {
    const navigate = useNavigate();

    const { formState, onInputChange } = useForm({
        username: "",
        password: "",
        isInvalid: false,
        errorMessage: "Usuario o contraseña incorrectos",
    });

    const { username, password, isInvalid, errorMessage } = formState;

    const handleSubmit = async (e) => {
        e.preventDefault();
        const loginService = new LoginService();
        const credentials = {
            username: username,
            password: password,
        };
        const response = await loginService.login(credentials);
        if (response.status === 200)
            navigate('/home');
        else{
            onInputChange({ target: {
                name: "errorMessage",
                value: response.detail,
            }});
            onInputChange({ target: {
                name: "isInvalid",
                value: true,
            }});
        }
    }   

    return (
        <>
            <form onSubmit={handleSubmit}>
                <h1 className='text-center'>Log In</h1>
                <input
                    name="username"
                    type="text"
                    value={username}
                    onChange={onInputChange}
                    placeholder="Username"
                    className='form-control mt-3'
                    required
                />
                <input
                    name="password"
                    type="password"
                    value={password}
                    onChange={onInputChange}
                    placeholder="Password"
                    className='form-control mt-3'
                    required
                />
                {isInvalid && <div className="alert alert-danger mt-3" role="alert">{errorMessage}</div>}
                <a href="/" className='text-center mt-1'>Forgot your password?</a>
                <button className='btn btn-primary mt-3'>Log In</button>
            </form>
        </>
    );
};

export default LoginForm;