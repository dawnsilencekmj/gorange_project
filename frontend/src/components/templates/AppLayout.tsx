import { Link, Outlet } from 'react-router-dom';

export default function AppLayout() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: 16 }}>
      <h1>RAS Web (Stock Proxy)</h1>
      <nav style={{ display: 'flex', gap: 12, marginBottom: 16 }}>
        <Link to="/">Home</Link>
        <Link to="/category">Category</Link>
        <Link to="/explorer">Explorer</Link>
        <Link to="/playground">Playground</Link>
      </nav>
      <Outlet />
    </div>
  );
}
