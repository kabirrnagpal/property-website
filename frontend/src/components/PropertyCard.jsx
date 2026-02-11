import React from 'react';
import { Card, CardContent } from './ui/card';
import { MapPin, Bed, Bath, Maximize, IndianRupee } from 'lucide-react';

const PropertyCard = ({ property }) => {
    const formatPrice = (price) => {
        if (price >= 10000000) {
            return `${(price / 10000000).toFixed(2)} Cr`;
        } else if (price >= 100000) {
            return `${(price / 100000).toFixed(2)} L`;
        } else {
            return price.toLocaleString('en-IN');
        }
    };

    return (
        <Card className="overflow-hidden hover:shadow-xl transition-all duration-300 cursor-pointer group">
            <div className="relative overflow-hidden">
                <img
                    src={property.image_url || 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800'}
                    alt={property.title}
                    className="w-full h-64 object-cover group-hover:scale-110 transition-transform duration-500"
                    onError={(e) => {
                        e.target.src = 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800';
                    }}
                />
                <div className="absolute top-4 right-4 bg-white px-3 py-1 rounded-full text-sm font-semibold shadow-md">
                    {property.property_type === 'rent' ? 'For Rent' : 'For Sale'}
                </div>
            </div>

            <CardContent className="p-5">
                <div className="flex items-start justify-between mb-3">
                    <h3 className="text-lg font-semibold text-gray-900 line-clamp-2 flex-1">
                        {property.title}
                    </h3>
                </div>

                <div className="flex items-center text-gray-600 mb-4">
                    <MapPin className="w-4 h-4 mr-1 flex-shrink-0" />
                    <span className="text-sm line-clamp-1">{property.address}</span>
                </div>

                <div className="flex items-center justify-between mb-4 pb-4 border-b">
                    <div className="flex items-center gap-4 text-gray-700">
                        <div className="flex items-center gap-1">
                            <Bed className="w-4 h-4" />
                            <span className="text-sm font-medium">{property.bedrooms}</span>
                        </div>
                        <div className="flex items-center gap-1">
                            <Bath className="w-4 h-4" />
                            <span className="text-sm font-medium">{property.bathrooms}</span>
                        </div>
                        <div className="flex items-center gap-1">
                            <Maximize className="w-4 h-4" />
                            <span className="text-sm font-medium">{property.area} sqft</span>
                        </div>
                    </div>
                </div>

                <div className="flex items-center justify-between">
                    <div className="flex items-center">
                        <IndianRupee className="w-5 h-5 text-primary font-bold" />
                        <span className="text-2xl font-bold text-primary">
                            {formatPrice(property.price)}
                        </span>
                        {property.property_type === 'rent' && (
                            <span className="text-sm text-gray-500 ml-1">/month</span>
                        )}
                    </div>
                </div>

                {property.amenities && property.amenities.length > 0 && (
                    <div className="mt-4 pt-4 border-t">
                        <div className="flex flex-wrap gap-2">
                            {property.amenities.slice(0, 3).map((amenity, index) => (
                                <span
                                    key={index}
                                    className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded-full"
                                >
                                    {amenity}
                                </span>
                            ))}
                            {property.amenities.length > 3 && (
                                <span className="text-xs text-gray-500 px-2 py-1">
                                    +{property.amenities.length - 3} more
                                </span>
                            )}
                        </div>
                    </div>
                )}
            </CardContent>
        </Card>
    );
};

export default PropertyCard;
