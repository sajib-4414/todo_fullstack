import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  // Check if accessToken and user data exist in localStorage
  const accessToken = localStorage.getItem('accessToken');
  const user = JSON.parse(localStorage.getItem('user'));
  const isSuperuser = localStorage.getItem('isSuperuser');

  const handleLogout = () => {
    // Remove accessToken, user data, and isSuperuser from localStorage
    localStorage.removeItem('accessToken');
    localStorage.removeItem('user');
    localStorage.removeItem('isSuperuser');
    // Redirect to the login page
    window.location.href = '/login';
  };

  return (
    <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <Link className="navbar-brand" to="">TodoList</Link>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>

      <div className="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul className="navbar-nav mr-auto">
          
          {accessToken && user ? (
            <>
              
              <li className="nav-item">
                <Link className="nav-link" to="/todos">Create Todo</Link>
              </li>
              {isSuperuser === 'true' && (
                <li className="nav-item">
                  <Link className="nav-link" to="/manageusers">Manage Users</Link>
                </li>
              )}
              <li className="nav-item">
                <span className="nav-link">{user.username}</span>
              </li>
              <li className="nav-item">
                <button className="btn btn-link nav-link" onClick={handleLogout}>Logout</button>
              </li>
            </>
          ) : (
            <>
              <li className="nav-item">
                <Link className="nav-link" to="/login">Login</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/register">Register</Link>
              </li>
            </>
          )}
        </ul>
      </div>
    </nav>
  );
}

export default Header;
