import './RegisterCourseForm.css';
import { useForm } from '../../../hooks/useForm';
import { useNavigate } from 'react-router-dom';
import RegisterCourseService from '../../../services/registerCourseService';

const RegisterCourseForm = () => {
    const navigate = useNavigate();

    const { formState, onInputChange } = useForm({
        name: '',
        description: '',
    });

    const { name, description, isInvalid, errorMessage} = formState;

    const validateForm = () => {
        let isValid = true;
        const requiredFields = [
            { name: 'name', message: 'Por favor, ingresa un nombre de curso.' },
            { name: 'description', message: 'Por favor, ingresa una descripción del curso.' }
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

        return isValid;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (validateForm()) {
            const registerCourseService = new RegisterCourseService();

            const course = {
                name: name,
                description: description
            };

            const response = await registerCourseService.registerCourse(course);

            if (response.status === 200)
                navigate('/home');
            else {
                onInputChange({
                    target: {
                        name: "errorMessage",
                        value: response.detail,
                    }
                });
                onInputChange({
                    target: {
                        name: "isInvalid",
                        value: true,
                    }
                });
            }

        }
    };

    return (
        <>
            <form onSubmit={handleSubmit} >
                <h1 className='text-center'>Register Course</h1>

                <input
                    name="name"
                    type="text"
                    value={name}
                    onChange={onInputChange}
                    placeholder="Course Name"
                    className='form-control mt-3'
                    required
                />

                <input
                    name="description"
                    type="text"
                    value={description}
                    onChange={onInputChange}
                    placeholder="Course Description"
                    className='form-control mt-3'
                    required
                />
                {isInvalid && <div className="alert alert-danger mt-3" role="alert">{errorMessage}</div>}
                <button type='submit' className='btn btn-primary mt-3'>
                    Register Course
                </button>
            </form>
        </>
    );
};

export default RegisterCourseForm;