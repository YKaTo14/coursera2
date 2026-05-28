const svgThumbnail = (bg, fg, label) => {
  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" width="320" height="220" viewBox="0 0 320 220">
      <defs>
        <linearGradient id="g" x1="0" y1="0" x2="0" y2="220" gradientUnits="userSpaceOnUse">
          <stop offset="0" stop-color="${bg}"/>
          <stop offset="1" stop-color="#ffffff"/>
        </linearGradient>
      </defs>
      <rect width="320" height="220" rx="22" fill="url(#g)"/>
      <circle cx="260" cy="52" r="24" fill="#ffffff" fill-opacity="0.45"/>
      <path d="M126 156C127 132 140 108 160 88C180 108 193 132 194 156C194 181 180 198 160 198C140 198 126 181 126 156Z" fill="${fg}"/>
      <path d="M88 164C90 138 105 113 130 95C143 118 150 143 150 167C150 188 138 203 120 203C102 203 87 186 88 164Z" fill="${fg}" fill-opacity="0.82"/>
      <path d="M170 167C170 144 177 118 190 95C215 113 230 138 232 164C233 186 218 203 200 203C182 203 170 188 170 167Z" fill="${fg}" fill-opacity="0.82"/>
      <rect x="96" y="175" width="128" height="18" rx="9" fill="#5C3A2E"/>
      <text x="160" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#143024">${label}</text>
    </svg>
  `;
  return `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`;
};

export const plantCatalog = [
  {
    id: "aloe-vera",
    name: "Aloe Vera",
    category: "Succulents",
    price: 18,
    thumbnail: svgThumbnail("#E2F4D8", "#5BA25E", "Aloe Vera"),
  },
  {
    id: "jade-plant",
    name: "Jade Plant",
    category: "Succulents",
    price: 22,
    thumbnail: svgThumbnail("#DCEFD7", "#4D9E68", "Jade Plant"),
  },
  {
    id: "snake-plant",
    name: "Snake Plant",
    category: "Succulents",
    price: 26,
    thumbnail: svgThumbnail("#D6F1E4", "#368D63", "Snake Plant"),
  },
  {
    id: "string-of-hearts",
    name: "String of Hearts",
    category: "Succulents",
    price: 20,
    thumbnail: svgThumbnail("#EAF8E6", "#5B9C63", "Hearts"),
  },
  {
    id: "echeveria",
    name: "Echeveria",
    category: "Succulents",
    price: 24,
    thumbnail: svgThumbnail("#E5F6E8", "#4E9D66", "Echeveria"),
  },
  {
    id: "haworthia",
    name: "Haworthia",
    category: "Succulents",
    price: 19,
    thumbnail: svgThumbnail("#EEF8F0", "#4D8A62", "Haworthia"),
  },
  {
    id: "peace-lily",
    name: "Peace Lily",
    category: "Tropical",
    price: 28,
    thumbnail: svgThumbnail("#ECF7F2", "#4B8E6C", "Peace Lily"),
  },
  {
    id: "monstera",
    name: "Monstera",
    category: "Tropical",
    price: 34,
    thumbnail: svgThumbnail("#E6F5E7", "#3D8455", "Monstera"),
  },
  {
    id: "bird-of-paradise",
    name: "Bird of Paradise",
    category: "Tropical",
    price: 38,
    thumbnail: svgThumbnail("#F1F8E7", "#487D4E", "Bird"),
  },
  {
    id: "rubber-plant",
    name: "Rubber Plant",
    category: "Tropical",
    price: 32,
    thumbnail: svgThumbnail("#E7F5EE", "#4C8F61", "Rubber"),
  },
  {
    id: "zz-plant",
    name: "ZZ Plant",
    category: "Tropical",
    price: 30,
    thumbnail: svgThumbnail("#ECF9E9", "#52925C", "ZZ Plant"),
  },
  {
    id: "dracaena",
    name: "Dracaena",
    category: "Tropical",
    price: 27,
    thumbnail: svgThumbnail("#EAF6EE", "#4C8A62", "Dracaena"),
  },
  {
    id: "air-plant",
    name: "Air Plant",
    category: "Air Plants",
    price: 16,
    thumbnail: svgThumbnail("#F1FBF4", "#69A88B", "Air Plant"),
  },
  {
    id: "string-of-pearls",
    name: "String of Pearls",
    category: "Air Plants",
    price: 24,
    thumbnail: svgThumbnail("#F4FBEE", "#709D55", "Pearls"),
  },
  {
    id: "boston-fern",
    name: "Boston Fern",
    category: "Air Plants",
    price: 19,
    thumbnail: svgThumbnail("#EEF8F0", "#4E8F69", "Fern"),
  },
  {
    id: "staghorn-fern",
    name: "Staghorn Fern",
    category: "Air Plants",
    price: 29,
    thumbnail: svgThumbnail("#F0FAF3", "#5A9A77", "Staghorn"),
  },
  {
    id: "moss-ball",
    name: "Moss Ball",
    category: "Air Plants",
    price: 14,
    thumbnail: svgThumbnail("#F4FAF0", "#6B9D61", "Moss Ball"),
  },
  {
    id: "venus-flytrap",
    name: "Venus Flytrap",
    category: "Air Plants",
    price: 21,
    thumbnail: svgThumbnail("#EEF8E9", "#5A9351", "Flytrap"),
  },
];

export const plantCategories = [...new Set(plantCatalog.map((plant) => plant.category))];
