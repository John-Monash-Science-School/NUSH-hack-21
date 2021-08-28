// note: this is ALL the code for every slot component.

const SlotsContext = createContext({
    named: {},
    changed: []
})

/*
    {
        named:{
            "foo":Component
        },
        changed:["foo"]
    }
*/

function Slot({name, children}) {
    const context = useContext(SlotsContext);
    const [content, setContent] = useState(children)

    // only run this code if the the "changed" array has changed in regards to the name.
    // note: this will run twice, once when name is added, and once when it is removed. (because the array changed both times)
    useEffect(()=>{
        
        setContent(context.named[name])

        // cleanup function, removes name from the array so we can change it later.
        return () => {
            context.changed = context.changed.filter((val)=>(val!=name))
            console.log(context)
        }
        
    }, [context.changed.filter((val)=>(val===name))])

    // checks if there is no SlotContent component defined for the specific name.
    if (context.named[name] === undefined) {
        return children
    } else {
        return content

    }
} 


function SlotContent({name,children}) {
    const context = useContext(SlotsContext)

    // defines the component
    context.named[name] = children
    // runs this code when the children change.
    useMemo(() => {
        // set slot value
        context.named[name] = children
        // add name to array so that Slot knows to update
        context.changed.push(name)
    }, [children]);

    //console.log(context)
    return null
}

function SlotProvider({children}) {
    const [named, setNamed] = useState({});
    const [changed, setChanged] = useState([]);
    
    return html`<${SlotsContext.Provider} value=${ {
        named, changed
    } }>
        ${children}
    <//>
    `
}

/* docs for slots:
<${Slot} name="foo">
    Fallback content
<//>
<${SlotContent} name="foo">
    content to replace the other one with.
<//>
*/

