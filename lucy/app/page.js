'use client'

import Image from 'next/image'
import styles from './page.module.css'
import logo from './images/fairy-temp.png'
import SearchComponent from './SearchComponent'

export default function Home() {
  return (
    <main className={styles.main}>
      <Image
              src={logo}
              alt='Lucy: Your Personal Travel Agent'
              className={styles.logo}
              priority
            />
    <SearchComponent></SearchComponent>
    </main>
  )
}
