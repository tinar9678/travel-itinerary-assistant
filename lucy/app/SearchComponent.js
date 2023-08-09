import React, { useState } from "react";
import './SearchComponent.css'

export default function SearchComponent() {
    const [inputString, setInputString] = useState("");
    const [filterselectedOption, setFilterSelectedOption] = useState(DURATIONS[0]);
    
    const handleInputChange = (value) => {
        setInputString(value);
    }
    
    const onSubmit = async (e) => {
        e.preventDefault();
        // fetch from python server here.
        const response = await fetch('http://127.0.0.1:5000/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message: inputString + "*" + filterselectedOption,
            })
        });
        const json = await response.json();
        console.log(json.data); // TODO(tinaryu): Set output itinerary component
    }

    return (
      <div className='search'>
        <form onSubmit={(e) => onSubmit(e)}>
            <input className='search-input' 
                placeholder='where do you want to go?' 
                onChange={(e) => handleInputChange(e.target.value)}>
            </input>
        </form>
        <DurationFilterComponent 
            filterselectedOption={filterselectedOption} 
            setFilterSelectedOption={setFilterSelectedOption}>
        </DurationFilterComponent>
      </div>
    )
}

function DurationFilterComponent({filterselectedOption, setFilterSelectedOption}) {
    const onFilterChange = (value) => {
        setFilterSelectedOption(value);
    }
    
    const filterOptions = DURATIONS.map((duration, id) => {
        const key = id+'-days';
        return (
            <option key={key} value={duration}>{duration}</option>
        )
    })

    return (
        <div className='duration-filter'>
            <label htmlFor="filter">Duration</label>
            <select className='filter' id='filter' value={filterselectedOption} onChange={(e) => onFilterChange(e.target.value)}>
                {filterOptions}
            </select>
        </div>
    )
}

const DURATIONS = ['1 day', '2 days', '3 days', '4 days', '5 days', '6 days'];