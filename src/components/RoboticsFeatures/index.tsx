import React from 'react';
import Link from '@docusaurus/Link';

const FeatureList = [
  {
    title: 'Advanced AI Integration',
    emoji: '🤖',
    description: (
      <>
        Seamlessly integrate cutting-edge AI models for intelligent decision-making and autonomous operation in robotics.
      </>
    ),
  },
  {
    title: 'Humanoid Robotics Platform',
    emoji: '⚡',
    description: (
      <>
        Develop and deploy sophisticated humanoid robots capable of complex interactions and tasks in diverse environments.
      </>
    ),
  },
  {
    title: 'Real-time Control Systems',
    emoji: '👁️',
    description: (
      <>
        Master the design and implementation of robust real-time control systems for precise robot movements and stability.
      </>
    ),
  },
  {
    title: 'Perception & Sensing',
    emoji: '🗺️',
    description: (
      <>
        Explore advanced perception techniques, including computer vision and LiDAR, to enable robots to understand their surroundings.
      </>
    ),
  },
  {
    title: 'Navigation & SLAM',
    emoji: '⚖️',
    description: (
      <>
        Implement state-of-the-art navigation algorithms and Simultaneous Localization and Mapping (SLAM) for autonomous exploration.
      </>
    ),
  },
  {
    title: 'Ethical AI & Robotics',
    emoji: '🛡️', // Using a shield emoji for ethics
    description: (
      <>
        Understand and apply ethical considerations in AI and robotics development to ensure responsible and beneficial innovations.
      </>
    ),
  },
];

function Feature({ title, emoji, description }) {
  return (
    <div className="flex flex-col items-center text-center p-4 border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200">
      <div className="text-5xl mb-4">{emoji}</div>
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  );
}

export default function RoboticsFeatures() {
  return (
    <section className="container mx-auto py-16 px-4">
      <div className="text-center mb-12">
        <h2 className="text-4xl font-bold text-gray-800 mb-4">Explore Our Robotics Features</h2>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          Discover the cutting-edge capabilities and innovative solutions we offer in the field of robotics.
        </p>
        <div className="mt-8 flex justify-center space-x-6"> {/* Horizontal spacing */}
          <Link
            className="button button--primary button--lg bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
            to="/docs/robotics/get-started">
            Get Started
          </Link>
          <Link
            className="button button--secondary button--lg bg-gray-200 hover:bg-gray-300 text-gray-800 font-semibold py-3 px-8 rounded-lg shadow-md transform hover:scale-105 transition-all duration-300"
            to="/docs/robotics/learn-more">
            Learn More
          </Link>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"> {/* Grid layout with spacing */}
        {FeatureList.map((props, idx) => (
          <Feature key={idx} {...props} />
        ))}
      </div>
    </section>
  );
}
