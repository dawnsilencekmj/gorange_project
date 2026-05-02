import { useEffect, useState } from 'react';
import { apiClient } from '../../shared/api/client';

export default function PlaygroundPage() {
  const [res, setRes] = useState<any>();
  useEffect(() => {
    apiClient.get('/playground/rule-demo?vol_threshold=0.01').then((r) => setRes(r.data));
  }, []);
  return <div><h2>Playground</h2><pre>{JSON.stringify(res, null, 2)}</pre></div>;
}
