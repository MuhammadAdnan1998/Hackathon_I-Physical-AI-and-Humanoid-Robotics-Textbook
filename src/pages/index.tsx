import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}> {/* Removed hero--primary */}
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary-cta button--lg" // Primary CTA button
            to="/docs/intro">
            Get Started
          </Link>
          <Link
            className="button button--secondary-cta button--lg" // Secondary CTA button
            to="/blog">
            Learn More
          </Link>
        </div>
      </div>
    </header>
  );
}

function HomepageCta() {
  return (
    <section className="ctaSection">
      <div className="container">
        <Heading as="h2" className="text--center">
          Ready to Build the Future of Robotics?
        </Heading>
        <div className="text--center">
          <Link
            className="button button--primary-cta button--lg"
            to="/docs/intro">
            Join the Movement
          </Link>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <HomepageCta /> {/* Added CTA section */}
      </main>
    </Layout>
  );
}
