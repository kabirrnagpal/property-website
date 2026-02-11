import React, { useState } from 'react';
import { Search, MapPin, Home, IndianRupee } from 'lucide-react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Select } from './ui/select';

const SearchBar = ({ onSearch }) => {
    const [filters, setFilters] = useState({
        city: '',
        property_type: '',
        min_budget: '',
        max_budget: ''
    });

    const handleFilterChange = (key, value) => {
        setFilters(prev => ({
            ...prev,
            [key]: value
        }));
    };

    const handleSearch = () => {
        const searchFilters = {};

        if (filters.city) searchFilters.city = filters.city;
        if (filters.property_type) searchFilters.property_type = filters.property_type;
        if (filters.min_budget) searchFilters.min_budget = parseInt(filters.min_budget);
        if (filters.max_budget) searchFilters.max_budget = parseInt(filters.max_budget);

        onSearch(searchFilters);
    };

    const handleReset = () => {
        setFilters({
            city: '',
            property_type: '',
            min_budget: '',
            max_budget: ''
        });
        onSearch({});
    };

    return (
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-8">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
                {/* City Selection */}
                <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-700 flex items-center gap-2">
                        <MapPin className="w-4 h-4" />
                        City
                    </label>
                    <Select
                        value={filters.city}
                        onChange={(e) => handleFilterChange('city', e.target.value)}
                    >
                        <option value="">All Cities</option>
                        <option value="Pune">Pune</option>
                        <option value="Hyderabad">Hyderabad</option>
                    </Select>
                </div>

                {/* Property Type */}
                <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-700 flex items-center gap-2">
                        <Home className="w-4 h-4" />
                        Property Type
                    </label>
                    <Select
                        value={filters.property_type}
                        onChange={(e) => handleFilterChange('property_type', e.target.value)}
                    >
                        <option value="">All Types</option>
                        <option value="rent">For Rent</option>
                        <option value="buy">For Sale</option>
                    </Select>
                </div>

                {/* Min Budget */}
                <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-700 flex items-center gap-2">
                        <IndianRupee className="w-4 h-4" />
                        Min Budget
                    </label>
                    <Input
                        type="number"
                        placeholder="Min"
                        value={filters.min_budget}
                        onChange={(e) => handleFilterChange('min_budget', e.target.value)}
                    />
                </div>

                {/* Max Budget */}
                <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-700 flex items-center gap-2">
                        <IndianRupee className="w-4 h-4" />
                        Max Budget
                    </label>
                    <Input
                        type="number"
                        placeholder="Max"
                        value={filters.max_budget}
                        onChange={(e) => handleFilterChange('max_budget', e.target.value)}
                    />
                </div>

                {/* Search Buttons */}
                <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-700 invisible">Action</label>
                    <div className="flex gap-2">
                        <Button
                            onClick={handleSearch}
                            className="flex-1 bg-primary hover:bg-primary/90"
                        >
                            <Search className="w-4 h-4 mr-2" />
                            Search
                        </Button>
                        <Button
                            onClick={handleReset}
                            variant="outline"
                            className="px-4"
                        >
                            Reset
                        </Button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SearchBar;
