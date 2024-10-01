import React from "react";

const About = () => {
  return (
    <div className="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8 pt-4 my-16 ">
      <section className="">
        <div className="px-4 mx-auto sm:px-6 lg:px-8 max-w-7xl">
          <div className="max-w-2xl mx-auto text-center">
            <h2 className="text-3xl font-bold leading-tight text-black sm:text-4xl lg:text-5xl">
              AI Scholar Summary
            </h2>
            <p className="max-w-md mx-auto mt-4 text-base leading-relaxed text-gray-600">
              AI Scholar Summary is driven by AI, it automatically summarizes
              academic articles and automatically visualizes and predicts the
              article data.
            </p>
            <br></br>
            <br></br>
          </div>
        </div>
      </section>
      <img className="mx-auto rounded-lg w-3/4" src="/summary.jpg" alt="" />
      <br></br>
      <br></br>
      <img className="mx-auto rounded-lg w-3/4" src="/data.jpg" alt="" />
    </div>
  );
};

export default About;
