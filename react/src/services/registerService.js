class RegisterService{
    constructor(){
        this.api_url = import.meta.env.VITE_API_URL;
    }

    async register(user){
        const response = await fetch(`${this.api_url}/users`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        if (!response.ok){
            const data = await response.json();
            let ans = {}
            ans['status'] = response.status;
            ans['detail'] = data.detail;
            return ans;
        }
        const data = await response.json();
        data['status'] = response.status;
        return data;
    }
}

export default RegisterService;