from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Data: Room Decor Suggestions
# Each vibe has a list of "Pins" (ideas)
decor_data = {
    "cozy": [
        {"title": "Warm Reading Nook", "desc": "A plush armchair with a chunky knit blanket, surrounded by warm fairy lights and stacked books.", "img_prompt": "cozy reading nook with fairy lights and chunky knit blanket"},
        {"title": "Hygge Bedroom", "desc": "Soft neutral tones, lots of textures, candles, and a low platform bed with linen sheets.", "img_prompt": "hygge bedroom with candles and linen sheets"},
        {"title": "Fireplace Gathering", "desc": "A faux fireplace with floor cushions and a sheepskin rug for intimate conversations.", "img_prompt": "cozy fireplace with floor cushions and sheepskin rug"},
        {"title": "Soft Lighting Setup", "desc": "Paper lanterns and dimmable warm bulbs to create a soothing atmosphere.", "img_prompt": "room with paper lanterns and warm soft lighting"},
    ],
    "minimalist": [
        {"title": "Monochrome Living", "desc": "Clean lines, white walls, and a single statement piece of furniture in black or grey.", "img_prompt": "minimalist living room monochrome white walls"},
        {"title": "Zen Workspace", "desc": "A decluttered desk with hidden cable management and a single bonsai tree.", "img_prompt": "minimalist workspace with bonsai tree"},
        {"title": "Open Space Concept", "desc": "Airy layout with functional furniture and zero clutter.", "img_prompt": "minimalist open space living room airy"},
        {"title": "Geometric Accents", "desc": "Simple geometric shapes in artwork or rugs to add interest without chaos.", "img_prompt": "minimalist room with geometric art"},
    ],
    "bohemian": [
        {"title": "Macramé Wall Art", "desc": "Handmade macramé hangings and plenty of indoor plants.", "img_prompt": "bohemian room with macrame wall hanging and plants"},
        {"title": "Pattern Clash", "desc": "Mix of persian rugs, colorful throw pillows, and ethnic patterns.", "img_prompt": "bohemian living room with colorful rugs and pillows"},
        {"title": "Rattan Furniture", "desc": "Peacock chairs or rattan side tables for that earthy, artistic feel.", "img_prompt": "bohemian room with rattan furniture"},
        {"title": "Canopy Bed", "desc": "Sheer fabric draped over the bed with hanging ivy.", "img_prompt": "bohemian canopy bed with ivy"},
    ],
    "industrial": [
        {"title": "Exposed Brick Wall", "desc": "Raw brick walls paired with metal shelving units.", "img_prompt": "industrial room with exposed brick wall and metal shelves"},
        {"title": "Edison Bulbs", "desc": "Hanging pendant lights with exposed filaments.", "img_prompt": "industrial lighting with edison bulbs"},
        {"title": "Leather & Metal", "desc": "Distressed leather sofa with a steel coffee table.", "img_prompt": "industrial living room leather sofa metal table"},
        {"title": "Concrete Floors", "desc": "Polished concrete flooring with a cowhide rug.", "img_prompt": "industrial room concrete floor cowhide rug"},
    ],
    "luxury": [
        {"title": "Velvet Elegance", "desc": "Deep jewel-toned velvet sofas and gold accents.", "img_prompt": "luxury living room velvet sofa gold accents"},
        {"title": "Marble Finishes", "desc": "Marble coffee tables or countertops for a premium look.", "img_prompt": "luxury room with marble coffee table"},
        {"title": "Crystal Chandelier", "desc": "A statement chandelier to act as the room's centerpiece.", "img_prompt": "luxury room with crystal chandelier"},
        {"title": "Floor-to-Ceiling Drapes", "desc": "Heavy, high-quality curtains that pool slightly on the floor.", "img_prompt": "luxury room with heavy floor to ceiling curtains"},
    ],
    "garden": [
        {"title": "Indoor Jungle", "desc": "Shelves filled with pothos, monstera, and ferns.", "img_prompt": "indoor jungle living room with many plants"},
        {"title": "Botanical Prints", "desc": "Wallpaper or framed art featuring vintage botanical illustrations.", "img_prompt": "room with botanical wallpaper"},
        {"title": "Natural Wood", "desc": "Live-edge wood furniture and green accents.", "img_prompt": "room with live edge wood furniture and plants"},
        {"title": "Terrariums", "desc": "Glass terrariums as centerpieces on tables.", "img_prompt": "room with glass terrariums on table"},
    ],
    "retro": [
        {"title": "Mid-Century Modern", "desc": "Teak sideboards and peg-legged furniture from the 50s/60s.", "img_prompt": "mid century modern living room"},
        {"title": "Funky Colors", "desc": "Mustard yellow, avocado green, and burnt orange color palette.", "img_prompt": "retro room with mustard yellow and orange colors"},
        {"title": "Vinyl Corner", "desc": "A record player setup with displayed album art.", "img_prompt": "retro room with vinyl record player station"},
        {"title": "Neon Sign", "desc": "Custom neon sign on the wall for a pop of vintage cool.", "img_prompt": "room with neon sign on wall"},
    ],
    "tech": [
        {"title": "RGB Lighting", "desc": "Customizable LED strips behind the desk and monitor.", "img_prompt": "gaming room with rgb lighting"},
        {"title": "Hexagon Panels", "desc": "Nanoleaf-style light panels on the wall.", "img_prompt": "tech room with hexagon light panels"},
        {"title": "Ergonomic Station", "desc": "High-end ergonomic chair and standing desk setup.", "img_prompt": "modern workspace with ergonomic chair and standing desk"},
        {"title": "Futuristic Shelving", "desc": "Floating shelves with backlighting to display gadgets.", "img_prompt": "futuristic room with floating backlit shelves"},
    ],
    "study": [
        {"title": "Distraction-Free Zone", "desc": "Clean white desk facing a window or blank wall.", "img_prompt": "minimalist study desk facing window"},
        {"title": "Organization Wall", "desc": "Pegboard or corkboard for notes, stationery, and calendar.", "img_prompt": "study room with pegboard organizer"},
        {"title": "Library Vibes", "desc": "Floor-to-ceiling bookshelves and a rolling ladder.", "img_prompt": "study room with floor to ceiling bookshelves"},
        {"title": "Focus Lighting", "desc": "Adjustable architect lamp for precise task lighting.", "img_prompt": "study desk with architect lamp"},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    vibe = request.form.get('vibe')
    # Get suggestions for the selected vibe, or a default mix if not found
    suggestions = decor_data.get(vibe, [])
    
    # If vibe not found or empty, just pick random ones (fallback)
    if not suggestions:
        all_suggestions = [item for sublist in decor_data.values() for item in sublist]
        suggestions = random.sample(all_suggestions, 4)

    return render_template('results.html', vibe=vibe, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
