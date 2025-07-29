import React, { useState } from 'react';
import axios from 'axios';

export const CreatePoolForm = () => {
  const [poolName, setPoolName] = useState('');
  const [address, setAddress] = useState('');
  const [district, setDistrict] = useState('');
  const [city, setCity] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [message, setMessage] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setMessage('');

    const token = localStorage.getItem('accessToken');
    if (!token) {
      setMessage("Lỗi: Bạn chưa đăng nhập hoặc phiên đã hết hạn.");
      setIsSubmitting(false);
      return;
    }

    const poolData = {
      name: poolName,
      address: address,
      district: district,
      city: city,
      phone: phone,
      email: email,
    };

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/pools/register',
        poolData,
        {
          headers: {
            'Authorization': `Bearer ${token}` // Gửi token để xác thực
          }
        }
      );

      setMessage(`Đăng ký thành công hồ bơi: "${response.data.name}"! Chúng tôi sẽ liên hệ với bạn sớm.`);

    } catch (error) {
      console.error("Lỗi khi đăng ký hồ bơi:", error);
      setMessage("Đã có lỗi xảy ra. Vui lòng thử lại.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div style={{ marginTop: '30px', padding: '20px', border: '1px solid #eee', borderRadius: '8px' }}>
      <h3>Đăng ký Hồ bơi của bạn - Bước 1/2</h3>
      <p>Cung cấp các thông tin cơ bản để chúng tôi xem xét và tạo tài khoản cho bạn.</p>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '20px' }}>
        <input
          type="text" placeholder="Tên hồ bơi (*)" value={poolName}
          onChange={(e) => setPoolName(e.target.value)}
          style={{ padding: '10px' }} required
        />
        {/* ... các input khác giữ nguyên ... */}
        <input
          type="text" placeholder="Địa chỉ chi tiết (*)" value={address}
          onChange={(e) => setAddress(e.target.value)}
          style={{ padding: '10px' }} required
        />
        <input
          type="text" placeholder="Quận/Huyện (*)" value={district}
          onChange={(e) => setDistrict(e.target.value)}
          style={{ padding: '10px' }} required
        />
        <input
          type="text" placeholder="Tỉnh/Thành phố (*)" value={city}
          onChange={(e) => setCity(e.target.value)}
          style={{ padding: '10px' }} required
        />
        <input
          type="text" placeholder="Số điện thoại liên hệ" value={phone}
          onChange={(e) => setPhone(e.target.value)}
          style={{ padding: '10px' }}
        />
        <input
          type="email" placeholder="Email liên hệ" value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{ padding: '10px' }}
        />
        <button type="submit" disabled={isSubmitting} style={{ padding: '10px', cursor: 'pointer', backgroundColor: '#007bff', color: 'white', border: 'none' }}>
          {isSubmitting ? 'Đang gửi...' : 'Gửi Đăng Ký'}
        </button>
        {message && <p style={{ marginTop: '15px', color: 'green' }}>{message}</p>}
      </form>
    </div>
  );
};