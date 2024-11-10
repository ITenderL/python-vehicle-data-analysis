import axios from 'axios'

const service = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  // baseURL: process.env.REACT_APP_API_URL,
  timeout: 5000
})

export default service