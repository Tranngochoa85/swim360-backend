import React from 'react';
import { CreatePoolForm } from '../components/CreatePoolForm'; // Import component mới

export const DashboardPage = () => {
  const token = localStorage.getItem('accessToken');

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    window.location.reload();
  };

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: 'auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2>Welcome to your Dashboard</h2>
        <button onClick={handleLogout} style={{ padding: '10px' }}>
          Logout
        </button>
      </div>
      <p>You are logged in!</p>

      <hr style={{ margin: '20px 0' }} />

      {/* Hiển thị component form tạo hồ bơi */}
      <CreatePoolForm />

    </div>
  );
};