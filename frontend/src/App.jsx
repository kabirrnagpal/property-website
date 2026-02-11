import React, { useState, useEffect } from 'react';
import SearchBar from './components/SearchBar';
import PropertyCard from './components/PropertyCard';
import { propertyApi } from './services/api';
import { Building2, Loader2 } from 'lucide-react';
import './index.css';

function App() {
    const [properties, setProperties] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchProperties = async (filters = {}) => {
        setLoading(true);
        setError(null);
        try {
            const data = await propertyApi.getProperties(filters);
            setProperties(data);
        } catch (err) {
            setError('Failed to load properties. Please make sure the backend server is running.');
            console.error('Error:', err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchProperties();
    }, []);

    const handleSearch = (filters) => {
        fetchProperties(filters);
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
            {/* Header */}
            <header className="bg-white shadow-sm sticky top-0 z-50">
                <div className="container mx-auto px-4 py-4">
                    <div className="flex items-center gap-3">
                        <Building2 className="w-8 h-8 text-primary" />
                        <div>
                            <h1 className="text-2xl font-bold text-gray-900">PropertySearch</h1>
                            <p className="text-sm text-gray-600">Find your dream home in Pune & Hyderabad</p>
                        </div>
                    </div>
                </div>
            </header>

            {/* Main Content */}
            <main className="container mx-auto px-4 py-8">
                {/* Search Bar */}
                <SearchBar onSearch={handleSearch} />

                {/* Results Section */}
                <div className="mb-6">
                    <h2 className="text-2xl font-bold text-gray-900 mb-2">
                        {loading ? 'Loading...' : `${properties.length} Properties Found`}
                    </h2>
                    <p className="text-gray-600">
                        Explore the best properties in Pune and Hyderabad
                    </p>
                </div>

                {/* Loading State */}
                {loading && (
                    <div className="flex items-center justify-center py-20">
                        <Loader2 className="w-12 h-12 text-primary animate-spin" />
                    </div>
                )}

                {/* Error State */}
                {error && !loading && (
                    <div className="bg-red-50 border border-red-200 rounded-lg p-6 text-center">
                        <p className="text-red-800 font-medium">{error}</p>
                        <p className="text-red-600 text-sm mt-2">
                            Make sure to run: <code className="bg-red-100 px-2 py-1 rounded">cd backend && python -m uvicorn main:app --reload</code>
                        </p>
                    </div>
                )}

                {/* Properties Grid */}
                {!loading && !error && properties.length > 0 && (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {properties.map((property) => (
                            <PropertyCard key={property.id} property={property} />
                        ))}
                    </div>
                )}

                {/* No Results */}
                {!loading && !error && properties.length === 0 && (
                    <div className="text-center py-20">
                        <Building2 className="w-16 h-16 text-gray-400 mx-auto mb-4" />
                        <h3 className="text-xl font-semibold text-gray-700 mb-2">No properties found</h3>
                        <p className="text-gray-500">Try adjusting your search filters</p>
                    </div>
                )}
            </main>

            {/* Footer */}
            <footer className="bg-white border-t mt-16">
                <div className="container mx-auto px-4 py-8">
                    <div className="text-center text-gray-600">
                        <p className="text-sm">© 2026 PropertySearch. All rights reserved.</p>
                        <p className="text-xs mt-2">Pune • Hyderabad</p>
                    </div>
                </div>
            </footer>
        </div>
    );
}

export default App;
