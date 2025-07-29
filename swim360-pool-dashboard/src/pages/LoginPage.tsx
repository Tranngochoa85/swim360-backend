import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

export const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); // Khởi tạo hook navigate

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();

    const params = new URLSearchParams();
    params.append('username', email);
    params.append('password', password);

    try {
      const response = await axios.post('http://172.20.10.2:8000/login', params);
      
      const accessToken = response.data.access_token;
      localStorage.setItem('accessToken', accessToken);
      
      // Dùng navigate để chuyển hướng đến trang chủ
      navigate('/');

    } catch (error) {
      console.error('Lỗi đăng nhập:', error);
      alert('Đăng nhập thất bại. Vui lòng kiểm tra lại email hoặc mật khẩu.');
    }
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '10px', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
        <h2>Swim360 Pool Partner Login</h2>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{ padding: '10px' }}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ padding: '10px' }}
          required
        />
        <button type="submit" style={{ padding: '10px', cursor: 'pointer' }}>
          Login
        </button>
      </form>
    </div>
  );
};