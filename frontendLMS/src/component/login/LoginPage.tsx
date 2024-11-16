import React, { useState } from 'react'
import eye from "../../svgFile/eye.svg"
import eyeslash from "../../svgFile/eyeslash.svg"
import backbutton from "../../svgFile/backbutton.svg"
const LoginPage = () => {
    const [toggletype, setToggletype] = useState<string>("password");
    const [erroremail, setErroremail] = useState<boolean>(false);
    const [email, setEmail] = useState<string>("");

    const emailvalidation = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = e.target.value;
        setEmail(newValue);
        var emailPattern = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
        if (!emailPattern.test(newValue)) {
            setErroremail(true);
        } else {
            setErroremail(false);
        }
    }
    const toggleeye = () => {
        if (toggletype === "password") {
            setToggletype("text")
        } if (toggletype === "text") {
            setToggletype("password")
        }
    }
    return (
        <>
            <div className='flex justify-center items-center h-screen '>
                <div className=' border-solid border border-neutral-500 rounded-md p-4 shadow-xl w-80 md:w-96'>

                    <div className='relative'>
                        <a href="#" className='absolute top-1/2 left-0 -translate-y-1/2'>
                            <img src={backbutton} />
                        </a>

                        <div className='text-center text-4xl font-semibold'>Login</div>
                    </div>

                    <div className='mt-6'>
                        <label htmlFor="email" className='block text-lg font-medium text-black'>Email</label>
                        <input type="text" name='email' value={email} onChange={emailvalidation} id='email' placeholder='Enter Email' className={erroremail ? ('text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border border-red-500 mt-1 w-full rounded-md') : ('text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md')} />
                        <span className={erroremail ? ('text-xs text-red-500 md:absolute block ') : ('text-xs text-red-500 md:absolute hidden')}  >Invalid Email</span>
                    </div>
                    <div className='mt-6'>
                        <label htmlFor="password" className=' block text-lg font-medium text-black'>Password</label>
                        <div className='relative'>
                            <div>
                                <input type={toggletype} name='password' id='password' placeholder='Enter Password' className='text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md' />
                            </div>
                            <div className='absolute top-1/2 right-2 -translate-y-1/2 mt-1'>
                                <button onClick={toggleeye}>
                                    {
                                        toggletype === "password" ? (<img src={eye} className='opacity-50' />) : (<img src={eyeslash} className='opacity-50' />)
                                    }


                                </button>
                            </div>
                        </div>
                    </div>
                    <div className='mt-3 flex justify-between items-center md:text-base text-sm '>
                        <div>
                            <input type="checkbox" id='rememberme' />
                            <label htmlFor="rememberme" className='mx-1'>Remember Me</label>
                        </div>
                        <div>
                            <a href="#" className='underline uppercase'>forget password?</a>
                        </div>
                    </div>
                    <div className='mt-3  flex items-center justify-center'>
                        <button type='submit' className='p-3 bg-black uppercase font-bold text-lg text-white border border-neutral-400 hover:bg-transparent hover:text-black  rounded-md w-80'>login</button>
                    </div>
                    <div className='mt-3 flex justify-center items-center'>
                        <div className='font-light text-lg uppercase'>-or-</div>
                    </div>
                    <div className='mt-3  flex items-center justify-center mb-2'>
                        <a href="/signup" className='p-3 text-center uppercase font-bold text-lg text-black border border-neutral-400 hover:bg-black hover:text-white rounded-md w-80' >create an account</a>
                    </div>
                </div>
            </div>
        </>
    )
}

export default LoginPage
