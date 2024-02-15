import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [errors, setErrors] = useState({});
  
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Form validation
    const newErrors = {};
    if (!formData.username) newErrors.username = 'Username is required';
    if (!formData.email) newErrors.email = 'Email is required';
    if (!formData.password) newErrors.password = 'Password is required';
    if (formData.password !== formData.confirmPassword) newErrors.confirmPassword = 'Passwords do not match';
    setErrors(newErrors);
    
    if (Object.keys(newErrors).length === 0) {
      // Form is valid, make Axios call
      axios.post('http://localhost:8001/auth/register/', formData)
        .then(response => {
          // Handle successful registration
          console.log(response.data);

          // Store user data and tokens in localStorage
          localStorage.setItem('user', JSON.stringify(response.data.user));
          localStorage.setItem('accessToken', response.data.token.access);
          localStorage.setItem('refreshToken', response.data.token.refresh);
          // Redirect to "/mytodos" page
          window.location = "/mytodos";
        })
        .catch(error => {
          // Handle error
          console.error('Registration error:', error);
        });
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="exampleInputUsername1">Username</label>
          <input
            type="text"
            className="form-control"
            id="exampleInputUsername1"
            name="username"
            value={formData.username}
            onChange={handleChange}
            placeholder="Enter Username"
          />
          {errors.username && <div className="text-danger">{errors.username}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="exampleInputEmail1">Email address</label>
          <input
            type="email"
            className="form-control"
            id="exampleInputEmail1"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Enter email"
          />
          {errors.email && <div className="text-danger">{errors.email}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="exampleInputPassword1">Password</label>
          <input
            type="password"
            className="form-control"
            id="exampleInputPassword1"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Password"
          />
          {errors.password && <div className="text-danger">{errors.password}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="exampleInputPassword2">Confirm Password</label>
          <input
            type="password"
            className="form-control"
            id="exampleInputPassword2"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            placeholder="Confirm Password"
          />
          {errors.confirmPassword && <div className="text-danger">{errors.confirmPassword}</div>}
        </div>
        <button type="submit" className="btn btn-primary">Register</button>
      </form>
    </div>
  );
};

export default Register;
