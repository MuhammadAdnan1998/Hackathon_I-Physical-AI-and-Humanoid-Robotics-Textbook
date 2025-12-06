import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
// Removed: import styles from './styles.module.css'; // Using global CSS

type FeatureItem = {
  title: string;
  emoji: string; // Changed from Svg to emoji
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Advanced AI Integration',
    emoji: '🧠',
    description: (
      <>
        Seamlessly integrate cutting-edge AI models for intelligent decision-making and autonomous operation in robotics.
      </>
    ),
  },
  {
    title: 'Humanoid Robotics Platform',
    emoji: '🤖',
    description: (
      <>
        Develop and deploy sophisticated humanoid robots capable of complex interactions and tasks in diverse environments.
      </>
    ),
  },
  {
    title: 'Real-time Control Systems',
    emoji: '⚡',
    description: (
      <>
        Master the design and implementation of robust real-time control systems for precise robot movements and stability.
      </>
    ),
  },
  {
    title: 'Perception & Sensing',
    emoji: '👁️',
    description: (
      <>
        Explore advanced perception techniques, including computer vision and LiDAR, to enable robots to understand their surroundings.
      </>
    ),
  },
  {
    title: 'Navigation & SLAM',
    emoji: '🗺️',
    description: (
      <>
        Implement state-of-the-art navigation algorithms and Simultaneous Localization and Mapping (SLAM) for autonomous exploration.
      </>
    ),
  },
  {
    title: 'Ethical AI & Robotics',
    emoji: '⚖️',
    description: (
      <>
        Understand and apply ethical considerations in AI and robotics development to ensure responsible and beneficial innovations.
      </>
    ),
  },
];

function Feature({title, emoji, description}: FeatureItem) { // Changed props
  return (
    <div className={clsx('col col--4', 'featureCard')}> {/* Added featureCard class */}
      <div className="text--center">
        <span className="emoji">{emoji}</span> {/* Render emoji */}
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className="features"> {/* Using global 'features' class */}
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
