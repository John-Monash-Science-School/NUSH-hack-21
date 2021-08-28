function Header () {
    return html`
        <header class="border-b-2 border-b_high pb-2 flex items-center">          
            <h1 class="text-xl"><a href="/" class="hover:opacity-80">Carbon Coins</a></h1>
            <div class="flex-grow"></div>
            <nav class="text-base">
                <${Slot} name="headerNav">
                    <a href="/login" class="px-2 py-1 bg-b_med ml-2 hover:bg-b_high inline-flex items-center content-center leading-none">
                        <span class="iconify mr-1 text-xl" data-icon="carbon:user-avatar"></span>
                        <span class="block">Login</span>
                    </a>
                    <a href="/search" class="px-2 py-1 bg-b_med ml-2 hover:bg-b_high inline-flex items-center content-center leading-none">
                        <span class="iconify mr-1 text-xl" data-icon="carbon:search-locate"></span>
                        <span class="block">Search</span>  
                    </a>
                    <a href="/calculator" class="px-2 py-1 bg-b_med ml-2 hover:bg-b_high inline-flex items-center content-center leading-none">
                        <span class="iconify mr-1 text-xl" data-icon="carbon:calculator"></span>
                        <span class="block">Calculate</span>
                    </a>
                <//>
            </nav>
        </header>
    `
}