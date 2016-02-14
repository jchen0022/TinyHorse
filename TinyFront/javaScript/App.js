import React from 'react';
import Tabs from './Tabs';

export default React.createClass({
    displayName: 'TinyHorse',
    getInitialState() {
       return {
           test:0
       }; 
    },
    render() {
        return (
            <div>
                <Tabs/>
            </div>    
        );
    }
});
    
