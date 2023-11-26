import '../assets/css/pages/registerCourse.css';
import RegisterCourseForm from '../components/registerCourse/RegisterCourseForm/RegisterCourseForm';

const RegisterCourse = () => {
    return (
        <div className="page-container">
            <div className="aside img-container">
                <div className="logo">
                </div>
            </div>
            <div className="main">
                <RegisterCourseForm />
            </div>
        </div>
    );
};

export default RegisterCourse;