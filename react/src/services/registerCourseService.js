class RegisterCourseService {
    constructor() {
        this.api_url = import.meta.env.VITE_API_URL;
    }

    async registerCourse(course) {
        const response = await fetch(`${this.api_url}/courses`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(course)
        });

        if (!response.ok) {
            const data = await response.json();
            return {
                status: response.status,
                detail: data.detail
            };
        }

        const data = await response.json();
        return {
            status: response.status,
            data: data
        };
    }
}

export default RegisterCourseService;