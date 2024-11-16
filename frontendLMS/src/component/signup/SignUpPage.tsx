import React, { useState } from "react";
// import { Link } from "react-router-dom"
import backbutton from '../../svgFile/backbutton.svg'
import eyeslash from '../../svgFile/eyeslash.svg'
import eye from '../../svgFile/eye.svg'
const SignUpPage = () => {
    const [toggletype, setToggletype] = useState<string>("password");
    const [checkpassword, setCheckpassword] = useState<boolean>(true);
    const [checkcpassword, setCheckcpassword] = useState<boolean>(true);
    const [erroremail, setErroremail] = useState<boolean>(false);
    const [errorphone, setErrorphone] = useState<boolean>(false);
    const [firstname, setFirstname] = useState<string>("");
    const [lastname, setLastname] = useState<string>("");
    const [email, setEmail] = useState<string>("");
    const [phone, setPhone] = useState<string>();
    const [password, setPassword] = useState<string>("");
    const [cpassword, setCpassword] = useState<string>("");

    const emailvalidation = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = e.target.value;
        setEmail(newValue);
        var emailPattern = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
        if (!emailPattern.test(newValue)) {
            setErroremail(true);
        } else {
            setErroremail(false);
        }
    };
    const phoneValidation = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = e.target.value;
        setPhone(newValue);
        if (newValue.length < 10 || newValue.length > 10 || /\-/.test(newValue)) {
            setErrorphone(true);
        } else {
            setErrorphone(false);
        }
    };

    const passwordvalidation = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = e.target.value;
        setPassword(newValue);

        if (
            newValue.length < 8 ||
            !newValue.match(/[0-9]/i) ||
            !newValue.match(/[A-Z]/) ||
            !newValue.match(/[a-z]/) ||
            !newValue.match(/[!@#$%^&*_?():;]/i)
        ) {
            setCheckpassword(false);
        } else {
            setCheckpassword(true);
        }
    };

    const confirmPasswordValid = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = e.target.value;
        setCpassword(newValue);
        if (password === newValue) {
            setCheckcpassword(true);
        } else {
            setCheckcpassword(false);
        }
    };

    const toggleeye = () => {
        if (toggletype === "password") {
            setToggletype("text");
        }
        if (toggletype === "text") {
            setToggletype("password");
        }
    };

    // console.log(firstname, lastname, email, password, phone);

    return (
        <>
            <div className="flex justify-center items-center h-screen">
                <div className="border border-neutral-500 rounded-md p-4  shadow-xl w-80 md:w-96">
                    <div className="relative">
                        <a href="#" className="absolute top-1/2 left-0 -translate-y-1/2">
                            <img src={backbutton} />
                        </a>
                        <div className="text-4xl text-center font-semibold">Sign-Up</div>
                    </div>
                    <div className="md:mt-3 mt:1 md:flex flex-col md:items-center md:justify-between md:gap-2 md:flex-row">
                        <div className="mb-2">
                            <label
                                htmlFor="firstname"
                                className="block text-lg font-medium text-black"
                            >
                                First Name
                            </label>
                            <input
                                type="text"
                                value={firstname}
                                onChange={(e) => setFirstname(e.target.value)}
                                name="firstname"
                                id="firstname"
                                placeholder="Enter First Name"
                                className="text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md"
                            />
                        </div>
                        <div className="mb-2">
                            <label
                                htmlFor="lastname"
                                className="block text-lg font-medium text-black"
                            >
                                Last Name
                            </label>
                            <input
                                type="text"
                                value={lastname}
                                onChange={(e) => setLastname(e.target.value)}
                                name="lastname"
                                id="lastname"
                                placeholder="Enter Last Name"
                                className="text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md"
                            />
                        </div>
                    </div>
                    <div className="md:mt-3 mt:1 md:flex flex-col md:items-center md:justify-between md:gap-2 md:flex-row">
                        <div className="mb-2">
                            <label
                                htmlFor="email"
                                className="block text-lg font-medium text-black"
                            >
                                Email
                            </label>
                            <input
                                type="text"
                                value={email}
                                onChange={emailvalidation}
                                name="email"
                                id="email"
                                placeholder="Enter Email"
                                className={
                                    erroremail
                                        ? "text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border border-red-500 mt-1 w-full rounded-md"
                                        : "text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md"
                                }
                            />
                            <span
                                className={
                                    erroremail
                                        ? "text-xs text-red-500 md:absolute block "
                                        : "text-xs text-red-500 md:absolute hidden"
                                }
                            >
                                Invalid Email
                            </span>
                        </div>
                        <div className="mb-2">
                            <label
                                htmlFor="mobilenumber"
                                className="block text-lg font-medium text-black"
                            >
                                Mobile Number
                            </label>
                            <input
                                type="number"
                                value={phone}
                                onChange={phoneValidation}
                                name="mobilenumber"
                                id="mobilenumber"
                                placeholder="Enter Mobile Number"
                                className={
                                    errorphone
                                        ? "phoneField text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border border-red-500 mt-1 w-full rounded-md"
                                        : "phoneField text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md"
                                }
                            />
                            <span
                                className={
                                    errorphone
                                        ? "text-xs text-red-500 md:absolute block "
                                        : "text-xs text-red-500 md:absolute hidden"
                                }
                            >
                                Invalid Phone Number
                            </span>
                        </div>
                    </div>
                    <div className="md:mt-3 mt:1 md:flex flex-col md:items-center md:justify-between md:gap-2 md:flex-row">
                        <div className="mb-2">
                            <label
                                htmlFor="password"
                                className="block text-lg font-medium text-black"
                            >
                                Password
                            </label>
                            <div className="relative">
                                <div>
                                    <input
                                        type={toggletype}
                                        value={password}
                                        onChange={passwordvalidation}
                                        name="password"
                                        id="password"
                                        placeholder="Enter password"
                                        className={
                                            checkpassword
                                                ? "text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md"
                                                : "text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border border-red-500 mt-1 w-full rounded-md"
                                        }
                                    />
                                </div>
                                <div className="absolute top-1/2 right-2 -translate-y-1/2 mt-1">
                                    <button onClick={toggleeye}>
                                        {toggletype === "password" ? (
                                            <img src={eye} className="opacity-50" />
                                        ) : (
                                            <img src={eyeslash} className="opacity-50" />
                                        )}
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div className="mb-2">
                            <label
                                htmlFor="confirmpassword"
                                className="block text-lg font-medium text-black"
                            >
                                Confirm Password
                            </label>
                            <input
                                type={toggletype}
                                value={cpassword}
                                onChange={confirmPasswordValid}
                                name="confirmpassword"
                                id="confirmpassword"
                                placeholder="Confirm Password"
                                className={
                                    checkcpassword
                                        ? "text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border focus:border-zinc-900 mt-1 w-full rounded-md"
                                        : "text-base px-2 py-1 focus:outline-none focus:ring-0 font-light border border-red-500 mt-1 w-full rounded-md"
                                }
                            />
                        </div>
                    </div>
                    <p
                        className={
                            checkpassword
                                ? "text-xs text-red-500 hidden"
                                : "text-xs text-red-500 block"
                        }
                    >
                        Password must be uppercase lowercase nummber and special charater
                    </p>
                    <p
                        className={
                            checkcpassword
                                ? "text-xs text-red-500 hidden"
                                : "text-xs text-red-500 block"
                        }
                    >
                        Password doesn't match
                    </p>
                    <div className="mt-3 text-base mx-4 md:mx-0 ">
                        <input type="checkbox" id="termandcondition" />
                        <label htmlFor="termandcondition" className="mx-1">
                            Accept all terms and condition
                        </label>
                    </div>
                    <div className="mt-3  flex items-center justify-center ">
                        <button
                            type="submit"
                            className="p-3 bg-black uppercase font-bold text-lg border border-neutral-500 text-white rounded-md w-60 md:w-80 hover:bg-transparent hover:text-black hover:border hover:border-neutral-500"
                        >
                            create an account
                        </button>
                    </div>
                    <div className="mt-3 text-base items-center justify-center flex mb-2">
                        <a href="/login" className=" text-blue-700 hover:text-black">
                            Already have an account
                        </a>
                    </div>
                </div>

            </div>
        </>
    )
}

export default SignUpPage
