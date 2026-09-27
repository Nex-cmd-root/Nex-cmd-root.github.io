/**
 * Verdant Greens - Home Page Spectacles & Botanical Variety Showcase Data
 * High-definition visual showcases demonstrating plant variety, lush bundles,
 * and interior styling without prices.
 */

const SPECTACLES = [
    {
        id: 'spec-01',
        title: 'The Grand Greenhouse Canopy',
        category: 'bundles',
        categoryLabel: 'Lush Bundles',
        image: 'images/spectacles/spectacle-main-attraction.webp',
        description: 'A harmonious grouping of broad Monstera, tall Palms, and variegated Aglaonemas creating a multi-layered rainforest microclimate.',
        tags: ['Monstera', 'Palms', 'Bundles', 'Living Room']
    },
    {
        id: 'spec-02',
        title: 'Architectural Desert & Purifier Duo',
        category: 'bundles',
        categoryLabel: 'Lush Bundles',
        image: 'images/spectacles/spectacle-air-purifiers-and-cacti.webp',
        description: 'Clean modern pairing of vertical Sansevieria swords with textured desert cacti in minimalist decorative planters.',
        tags: ['Sansevieria', 'Cactus', 'Modern', 'Purifier']
    },
    {
        id: 'spec-03',
        title: 'Vibrant Aglaonema & Croton Cluster',
        category: 'varieties',
        categoryLabel: 'Variety Showcase',
        image: 'images/spectacles/spectacle-crotons.webp',
        description: 'Showcasing the spectrum of tropical foliage colors: radiant amber, deep ruby, emerald green, and creamy silver accents.',
        tags: ['Crotons', 'Aglaonema', 'Colorful Foliage', 'Exotic']
    },
    {
        id: 'spec-04',
        title: 'Greenhouse Focal Point Ensemble',
        category: 'focal',
        categoryLabel: 'Statement Focals',
        image: 'images/spectacles/spectacle-focal-point.webp',
        description: 'Stately specimen plants arranged to create high visual interest and natural depth in luxury entrance foyers and executive spaces.',
        tags: ['Focal Point', 'Statement', 'Luxury', 'Ndola Greenhouse']
    },
    {
        id: 'spec-05',
        title: 'Sculptural Agave Americana Display',
        category: 'focal',
        categoryLabel: 'Statement Focals',
        image: 'images/spectacles/spectacle-agavi-4.webp',
        description: 'Striking geometric rosette forms that thrive in sunny verandas and bright architectural alcoves with minimal watering.',
        tags: ['Agave', 'Drought Hardy', 'Architectural', 'Desert']
    },
    {
        id: 'spec-06',
        title: 'King George Royal Sword Vertical Stand',
        category: 'focal',
        categoryLabel: 'Statement Focals',
        image: 'images/spectacles/spectacle-king-georges-sword.webp',
        description: 'Majestic cylindrical spears rising with commanding vertical elegance. Outstanding natural air-purifying capability.',
        tags: ['Sansevieria Stuckyi', 'King George', 'Air Purifier', 'Vertical']
    },
    {
        id: 'spec-07',
        title: 'Tropical Traveller’s Palm Fan Grandeur',
        category: 'focal',
        categoryLabel: 'Statement Focals',
        image: 'images/spectacles/spectacle-travellers-palm.webp',
        description: 'Iconic symmetrical fan foliage that immediately evokes an exotic island paradise in bright, spacious interior spaces.',
        tags: ['Traveller’s Palm', 'Tropical', 'Pet Safe', 'Fan Foliage']
    },
    {
        id: 'spec-08',
        title: 'Dense Aglaonema Silver Queen Colony',
        category: 'varieties',
        categoryLabel: 'Variety Showcase',
        image: 'images/spectacles/spectacle-agronimas.webp',
        description: 'Shade-loving silver foliage forming a dense, lush carpet. Perfect for enhancing indoor air quality in bedrooms and study nooks.',
        tags: ['Aglaonema', 'Silver Queen', 'Shade Loving', 'Clean Air']
    },
    {
        id: 'spec-09',
        title: 'Curated Multi-Tier Plant Stand Display',
        category: 'bundles',
        categoryLabel: 'Lush Bundles',
        image: 'images/spectacles/spectacle-display-image-1.webp',
        description: 'Demonstrating how layering tabletop succulents with mid-height foliage and tall statement palms creates an organic living wall.',
        tags: ['Plant Stand', 'Layered Styling', 'Home Decor', 'Living Wall']
    },
    {
        id: 'spec-10',
        title: 'Glossy Rubber Tree & Peace Lily Harmony',
        category: 'bundles',
        categoryLabel: 'Lush Bundles',
        image: 'images/spectacles/spectacle-display-image-2.webp',
        description: 'Deep burgundy broad leaves paired with variegated Peace Lily foliage and white floral spathes in a balanced interior vignette.',
        tags: ['Rubber Tree', 'Peace Lily', 'Foliage Combo', 'Vibrant']
    },
    {
        id: 'spec-11',
        title: 'Ruay Sub Prosperity & Fortune Bush',
        category: 'varieties',
        categoryLabel: 'Variety Showcase',
        image: 'images/spectacles/spectacle-ruay-sub.webp',
        description: 'Celebrated symbol of growth and prosperity. Dappled white speckles on thick waxy leaves that bring elegance to desks and side tables.',
        tags: ['Ruay Sub', 'Prosperity', 'Office Desk', 'Easy Care']
    },
    {
        id: 'spec-12',
        title: 'Exotic Madagascar Vanilla Orchid Vine',
        category: 'varieties',
        categoryLabel: 'Variety Showcase',
        image: 'images/spectacles/spectacle-vanilla-vine.webp',
        description: 'Fleshy succulent climbing foliage of the true vanilla orchid. Adds an exotic cascading vertical green touch to sunny indoor trellises.',
        tags: ['Vanilla Vine', 'Climbing Orchid', 'Rare', 'Cascading']
    },
    {
        id: 'spec-13',
        title: 'Indestructible Zamioculcas (ZZ) Suite',
        category: 'varieties',
        categoryLabel: 'Variety Showcase',
        image: 'images/spectacles/spectacle-zizi.webp',
        description: 'Glossy, polished emerald stems that flourish in low-light corridors and withstand missed waterings with effortless grace.',
        tags: ['ZZ Plant', 'Zizi', 'Low Light', 'Indestructible']
    },
    {
        id: 'spec-14',
        title: 'Sweet Berry Bush Ornamental Foliage',
        category: 'varieties',
        categoryLabel: 'Variety Showcase',
        image: 'images/spectacles/spectacle-berry-bush.webp',
        description: 'Compact decorative indoor shrub with scalloped evergreen leaves and cheerful berry clusters for dining tables and kitchens.',
        tags: ['Berry Bush', 'Ardisia', 'Decorative', 'Dining Room']
    },
    {
        id: 'spec-15',
        title: 'Greenhouse Specimen Showcase Panorama',
        category: 'greenhouse',
        categoryLabel: 'Greenhouse Life',
        image: 'images/spectacles/spectacle-display-image-8.webp',
        description: 'Rows of acclimatized tropical indoor plants nurtured in Ndola, ready for seamless transition into your home or office space.',
        tags: ['Nursery', 'Ndola', 'Acclimatized', 'Copperbelt']
    },
    {
        id: 'spec-16',
        title: 'Desert Cactus & Architectural Succulent Bed',
        category: 'varieties',
        categoryLabel: 'Variety Showcase',
        image: 'images/spectacles/spectacle-large-cactus.webp',
        description: 'Sun-drenched desert species displaying bold geometric ribs and sculptural textures that need watering only once a month.',
        tags: ['Columnar Cactus', 'Desert', 'Sun Lover', 'Low Water']
    }
];

window.VG_SPECTACLES = SPECTACLES;
