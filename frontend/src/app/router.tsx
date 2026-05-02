import { createBrowserRouter } from 'react-router-dom';
import HomePage from '../pages/Home';
import CategoryAnalyticsPage from '../pages/CategoryAnalytics';
import DataExplorerPage from '../pages/DataExplorer';
import PlaygroundPage from '../pages/Playground';

export const router = createBrowserRouter([
  { path: '/', element: <HomePage /> },
  { path: '/category', element: <CategoryAnalyticsPage /> },
  { path: '/explorer', element: <DataExplorerPage /> },
  { path: '/playground', element: <PlaygroundPage /> },
]);
