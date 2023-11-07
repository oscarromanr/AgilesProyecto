import './RegisterForm.css';
import { useState } from 'react';
import { useForm } from '../../../hooks/useForm';
import { useNavigate } from 'react-router-dom';
import { IconButton, InputAdornment, TextField } from '@mui/material';
import { Visibility, VisibilityOff } from '@mui/icons-material';

const RegisterForm = () => {
    const navigate = useNavigate();
    const [passwordError, setPasswordError] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);

    const { formState, onInputChange } = useForm({
        username: '',
        email: '',
        firstName: '',
        lastName: '',
        password: '',
        confirmPassword: '',
        isInvalid: false,
        errorMessage: '',
    });

    const { username, email, firstName, lastName, password, confirmPassword, isInvalid, errorMessage } = formState;

    const validateForm = () => {
        let isValid = true;
        const requiredFields = [
          { name: 'username', message: 'Por favor, ingresa un nombre de usuario.' },
          { name: 'email', message: 'Por favor, ingresa un correo electrónico.' },
          { name: 'firstName', message: 'Por favor, ingresa tu nombre.' },
          { name: 'lastName', message: 'Por favor, ingresa tu apellido.' },
          { name: 'password', message: 'Por favor, ingresa una contraseña.' },
          { name: 'confirmPassword', message: 'Por favor, confirma tu contraseña.' },
        ];
      
        for (const field of requiredFields) {
          if (!formState[field.name]) {
            onInputChange({
              target: {
                name: 'errorMessage',
                value: field.message,
              },
            });
            isValid = false;
          }
        }
      
        if (password.length < 8) {
          setPasswordError(true);
          isValid = false;
        }
      
        if (password !== confirmPassword) {
          onInputChange({
            target: {
              name: 'errorMessage',
              value: 'Las contraseñas no coinciden.',
            },
          });
          isValid = false;
        }
      
        return isValid;
      };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (validateForm()) {
            //Aqui llamar la API (Backend)
            navigate('/', { state: { successMessage: 'Usuario registrado exitosamente. Por favor, inicia sesión.' } });
        } else {
            onInputChange({
                target: {
                    name: 'isInvalid',
                    value: true,
                },
            });
        }
    };

    const togglePasswordVisibility = () => {
        setShowPassword((prevShowPassword) => !prevShowPassword);
    };

    const toggleConfirmPasswordVisibility = () => {
        setShowConfirmPassword((prevShowConfirmPassword) => !prevShowConfirmPassword);
    };

    return (
        <>
            <form onSubmit={handleSubmit} className='needs-validation' novalidate>
                <h1 className='text-center'>Register account</h1>
                {(passwordError || isInvalid) && (
                    <div className='alert alert-danger alert-dismissible fade show d-inline-block mt-3' role='alert'>
                        {passwordError && <div>La contraseña debe tener al menos 8 caracteres.</div>}
                        {isInvalid && <div>{errorMessage}</div>}
                    </div>
                )}

                <TextField
                    size='small'
                    name='username'
                    type='text'
                    value={username}
                    onChange={onInputChange}
                    placeholder="Username"
                    className='form-control mt-3'
                    required
                />

                <TextField
                    size='small'
                    name='email'
                    type='email'
                    value={email}
                    onChange={onInputChange}
                    placeholder='Email'
                    className='form-control mt-3'
                    required
                />

                <TextField
                    size='small'
                    name='firstName'
                    type='text'
                    value={firstName}
                    onChange={onInputChange}
                    placeholder='First Name'
                    className='form-control mt-3'
                    required
                />

                <TextField
                    size='small'
                    name='lastName'
                    type='text'
                    value={lastName}
                    onChange={onInputChange}
                    placeholder='Last Name'
                    className='form-control mt-3'
                    required
                />

                <TextField
                    size='small'
                    name='password'
                    type={showPassword ? 'text' : 'password'}
                    value={password}
                    onChange={onInputChange}
                    placeholder='Password'
                    className={`form-control mt-3 ${passwordError ? 'error' : ''}`}
                    required
                    InputProps={{
                        endAdornment: (
                            <InputAdornment position='end'>
                                <IconButton onClick={togglePasswordVisibility}>
                                    {showPassword ? <VisibilityOff /> : <Visibility />}
                                </IconButton>
                            </InputAdornment>
                        ),
                    }}
                />

                <TextField
                    size='small'
                    name='confirmPassword'
                    type={showConfirmPassword ? 'text' : 'password'}
                    value={confirmPassword}
                    onChange={onInputChange}
                    placeholder='Confirm Password'
                    className='form-control mt-3'
                    required
                    InputProps={{
                        endAdornment: (
                            <InputAdornment position='end'>
                                <IconButton onClick={toggleConfirmPasswordVisibility}>
                                    {showConfirmPassword ? <VisibilityOff /> : <Visibility />}
                                </IconButton>
                            </InputAdornment>
                        ),
                    }}
                />

                <button type='submit' className='btn btn-primary mt-3'>
                    Register
                </button>
            </form>
        </>
    );
};

export default RegisterForm;