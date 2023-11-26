import { useNavigate } from "react-router-dom";

class LoginService{
    constructor(){
        this.api_url = import.meta.env.VITE_API_URL;
    }

    async login(user){
        //transform user json to x-www-form-urlencoded
        const formBody = Object.keys(user).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(user[key])).join('&');
        const response = await fetch(`${this.api_url}/auth`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formBody
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
        localStorage.setItem('token', data.token);
        localStorage.setItem('user', JSON.stringify(data.user));
        return data;
    }
}

export default LoginService;