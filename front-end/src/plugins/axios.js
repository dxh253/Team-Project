import axios from 'axios';
    const getAPI = axios.create({
    baseURL: 'https://team22-22.bham.team',
    });

export { getAPI };
