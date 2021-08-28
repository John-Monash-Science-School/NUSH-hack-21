function Header () {
    return html`
        <header class="border-b-2 border-b_high pb-2 flex items-center">          
            <h1 class="text-xl"><a href="/" class="hover:opacity-80">Carbon Coins</a></h1>
            <div class="flex-grow"></div>
            <nav class="text-base">
                <a href="/login" class="px-2 py-1 bg-b_med ml-2 hover:bg-b_high inline-flex items-center">
                    <span class="iconify mr-1 text-xl" data-icon="carbon:user-avatar"></span>
                    login
                </a>
                <a href="#" class="px-2 py-1 bg-b_med ml-2 hover:bg-b_high inline-flex items-center">
                    <span class="iconify mr-1 text-xl" data-icon="carbon:share-knowledge"></span>
                    trade
                </a>
                <a href="/calculator" class="px-2 py-1 bg-b_med ml-2 hover:bg-b_high inline-flex items-center">
                    <span class="iconify mr-1 text-xl" data-icon="carbon:calculator"></span>
                    calculate
                </a>
            </nav>
        </header>
    `
}