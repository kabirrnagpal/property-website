const API_BASE_URL = 'http://localhost:8000';

export const propertyApi = {
    async getProperties(filters = {}) {
        const params = new URLSearchParams();

        if (filters.city) params.append('city', filters.city);
        if (filters.property_type) params.append('property_type', filters.property_type);
        if (filters.min_budget) params.append('min_budget', filters.min_budget);
        if (filters.max_budget) params.append('max_budget', filters.max_budget);

        const url = `${API_BASE_URL}/api/properties${params.toString() ? '?' + params.toString() : ''}`;

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Failed to fetch properties');
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching properties:', error);
            throw error;
        }
    },

    async getPropertyById(id) {
        try {
            const response = await fetch(`${API_BASE_URL}/api/properties/${id}`);
            if (!response.ok) {
                throw new Error('Failed to fetch property');
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching property:', error);
            throw error;
        }
    },

    async getCities() {
        try {
            const response = await fetch(`${API_BASE_URL}/api/cities`);
            if (!response.ok) {
                throw new Error('Failed to fetch cities');
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching cities:', error);
            throw error;
        }
    }
};
