// src/App.jsx
import Chat from './components/Chat'

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-3xl mx-auto py-4 px-4">
          <h1 className="text-2xl font-bold text-gray-900">AI Chat Assistant</h1>
        </div>
      </header>
      <main className="container mx-auto">
        <Chat />
      </main>
    </div>
  )
}

export default App
